# Icons

SVGs in this directory are mapped to CSS variables by `conf.py`.

For example, `wrench.svg` becomes `--icon-wrench-url`.

To add [a lucide icon](https://lucide.dev/icons/), matching the ones that Shibuya itself ships:

```
curl -L -o source/_icons/<name>.svg https://unpkg.com/lucide-static@latest/icons/<name>.svg
```
