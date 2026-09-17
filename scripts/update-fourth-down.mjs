import { cpSync, existsSync, mkdirSync, renameSync, rmSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFileSync } from 'node:child_process';

const portfolio = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const source = resolve(process.argv[2] ?? resolve(portfolio, '../fourth-down-calc'));
const output = resolve(source, 'dist/client');
const destination = resolve(portfolio, 'public/fourth-down-calc');
const staging = resolve(portfolio, '.astro/fourth-down-staging');

execFileSync('npm', ['run', 'build'], {
  cwd: source,
  env: { ...process.env, BASE_PATH: '', STATIC_ASSET_PREFIX: '/fourth-down-calc' },
  stdio: 'inherit',
});
for (const name of ['index.html', 'models/manifest.json', 'fourth-down-calc/_next']) {
  if (!existsSync(resolve(output, name))) throw new Error(`Missing calculator export: ${name}`);
}
rmSync(staging, { recursive: true, force: true });
mkdirSync(staging, { recursive: true });
cpSync(resolve(output, 'fourth-down-calc'), staging, { recursive: true });
for (const name of ['index.html', 'models', 'favicon.svg']) {
  cpSync(resolve(output, name), resolve(staging, name), { recursive: true });
}
cpSync(resolve(source, 'THIRD_PARTY_NOTICES.md'), resolve(staging, 'THIRD_PARTY_NOTICES.md'));
rmSync(destination, { recursive: true, force: true });
renameSync(staging, destination);
console.log('Updated public/fourth-down-calc. Run npm run build to validate the portfolio.');
