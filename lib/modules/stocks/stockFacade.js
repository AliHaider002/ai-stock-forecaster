const { spawn } = require("child_process");
const fs = require("fs");
const path = require("path");
const csv = require("csv-parser");

const collectData = () => {
  return new Promise((resolve, reject) => {
    try {
      let outputData = "";
      let html_url =
        "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies";
      const childProcess = spawn("python", ["scripts/snp.py", html_url]);

      childProcess.stdout.on("data", (data) => {
        outputData += data.toString(); // Accumulate data as string
      });

      childProcess.stderr.on("data", (data) => {
        console.error("stderr:", data.toString());
      });

      childProcess.on("close", (code) => {
        if (code === 0) {
          try {
            // Replace single quotes with double quotes to make it JSON-compatible
            let jsonString = outputData.replace(/'/g, '"');

            // Parse the string into a JavaScript array
            let resp = JSON.parse(jsonString);

            // Resolve with a single data key
            resolve(resp);
          } catch (parseError) {
            console.error("Error parsing result:", parseError);
            reject({
              data: [],
              message: "Parsing Error",
            });
          }
        } else {
          reject({
            data: [],
            message: `Python script exited with code ${code}`,
          });
        }
      });
    } catch (error) {
      console.error("Error:", error);
      reject(error);
    }
  });
};

// const newsDetector = () => {
//   return new Promise((resolve, reject) => {
//     try {
//       const childProcess = spawn("python", ["scripts/fake_news_detector.py"]);

//       childProcess.stdout.on("data", (data) => {
//         console.log("Result: ", data.toString());
//       });

//       childProcess.stderr.on("data", (data) => {
//         console.log("errorCheck", data.toString());
//       });

//       childProcess.on("close", (code) => {
//         console.log(`Child Process is closed with code: ${code}`);

//         // Read the predictions from the CSV file
//         const data = [];
//         fs.createReadStream(path.resolve("uploads/news_predictions.csv"))
//           .pipe(csv())
//           .on("data", (data) => results.push(data))
//           .on("end", () => {
//             resolve(results); // Resolve the promise with the results
//           })
//           .on("error", (error) => {
//             reject(error); // Reject the promise on error
//           });
//       });
//     } catch (error) {
//       reject(error); // Reject the promise on error
//     }
//   });
// };

// newsDetector();

module.exports = {
  collectData,
  // newsDetector,
};
