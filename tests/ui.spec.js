const { test, expect } = require('@playwright/test');
const path = require('path');

const repoRoot = path.join(__dirname, '..');

test.describe('CivStack UI Pages', () => {

  test('capability-router.html should recommend deterministic controller for high safety & hrt latency', async ({ page }) => {
    const filePath = 'file://' + path.join(repoRoot, 'tools/capability-router.html');
    await page.goto(filePath);

    // Verify title
    await expect(page).toHaveTitle(/Capability Router/);

    // Initial check
    await expect(page.locator('#rTier')).toContainText('SLM / VLA policy on-device');

    // Change safety to high
    await page.selectOption('#safety', 'high');
    // Change latency to hrt
    await page.selectOption('#latency', 'hrt');

    // Verify update
    await expect(page.locator('#rTier')).toContainText('Deterministic controller');
    await expect(page.locator('#rFallback')).toContainText('Verified safe-stop');
  });

  test('excellence-map.html should load sample baseline', async ({ page }) => {
    const filePath = 'file://' + path.join(repoRoot, 'tools/excellence-map.html');
    await page.goto(filePath);

    await expect(page).toHaveTitle(/Excellence Map/);

    // Click sample baseline
    await page.click('#sampleBtn');

    // Check if rows are populated and display numeric scores
    await expect(page.locator('.domain-row').first()).toBeVisible();
    await expect(page.locator('.domain-score').first()).toContainText('/');
  });

  test('work-system-mapper.html should recommend and generate record', async ({ page }) => {
    const filePath = 'file://' + path.join(repoRoot, 'tools/work-system-mapper.html');
    await page.goto(filePath);

    await expect(page).toHaveTitle(/Work-System Mapper/);

    // Input outcome & owner
    await page.fill('#outcome', 'Manage water quality');
    await page.fill('#owner', 'John Doe');

    // Select first friction
    await page.check('input[data-friction="0"]');

    // Click apply recommendations
    await page.click('#recommend');

    // Generate record
    await page.click('#generate');

    // Check generated record content
    const recordVal = await page.inputValue('#record');
    expect(recordVal).toContain('Manage water quality');
    expect(recordVal).toContain('John Doe');
    expect(recordVal).toContain('Role: Evidence & research enablement agent');
  });

  test('site/index.html search filter should work', async ({ page }) => {
    const filePath = 'file://' + path.join(repoRoot, 'site/index.html');
    await page.goto(filePath);

    await expect(page).toHaveTitle(/CivStack/);

    // Verify initial count
    await expect(page.locator('#count')).toContainText('416 / 416 skills');

    // Fill query
    await page.fill('#q', 'water');

    // Verify filtered count
    await expect(page.locator('#count')).toContainText('17 / 416 skills');
  });

});
