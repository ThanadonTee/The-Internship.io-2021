const puppeteer = require("puppeteer");
const express = require("express");
const app = express();

const data = async () => {
  const companyArr = [];
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto("https://theinternship.io/");

  try {
    await page.waitForSelector(".partner");
    const companyElementArr = await page.$$(".partner");
    for (const company of companyElementArr) {
      const companyObj = await {
        logo: await company.$eval(".logo-box a img", (img) =>
          img.getAttribute("src")
        ),
        text: await company.$eval(
          ".box-textbox .list-company",
          (text) => text.innerHTML
        ),
      };
      companyArr.push(companyObj);
    }
    browser.close();
    companyArr.sort((a, b) => {
      return a.text.length - b.text.length;
    });
    return companyArr;
  } catch (err) {
    console.log(err);
  }
};

app.get("/companies", async (req, res, next) => {
  data().then((data) => {
    const companyWrapper = {
      companies: [],
    };
    data.forEach((company) => {
      companyWrapper.companies.push({
        logo: "https://theinternship.io/" + company.logo,
      });
    });
    return res.json(companyWrapper);
  });
});

app.listen(3000, () => {
  console.log("Server is up on http://localhost:3000");
});
