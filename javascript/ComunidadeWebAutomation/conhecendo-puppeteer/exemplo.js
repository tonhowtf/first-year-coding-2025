const puppeteer = require('puppeteer')

const url = 'https://www.airbnb.com/';

(async () => {
  const browser = await puppeteer.launch({
    headless: false,
    defaultViewport: null,
    args: [
      '--use-fake-ui-for-media-stream',
      '--use-fake-device-for-media-stream',
      '--disable-features=site-per-process'
    ]

  });
  const context = browser.defaultBrowserContext();
  await context.overridePermissions(url, ['geolocation']);

  const page = await browser.newPage();

  await page.setGeolocation({
    latitude: 25.7751,
    longitude: -80.2105
  })
  await page.goto(url);
})()