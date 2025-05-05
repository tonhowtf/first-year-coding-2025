const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    headless: false,
    defaultViewport: null
    //slowMo: 300
  })

  const context = await browser.createIncognitoBrowserContext();
  const page = await context.newPage();
  await page.setViewport({
    width: 1920,
    height: 1080
  })
  await page.goto('https://www.reddit.com/r/puzzlevideogames/comments/1kfjdxw/blue_prince_a_masterpiece_with_many_layers/')

  await page.screenshot({ path: 'reddit.png', fullPage: true })
  //await browser.close()
})()