# WorldEdit Documentation

These are the files for WorldEdit's documentation.

Contributions are welcome. Please read the licensing information below.

## License

The documentation located under the "source" directory is licensed with the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Graphic assets and other materials, especially in regards to logos and other trademarks, are the property of their respective copyright owners and distribution may be restricted.

Contributions in regards to the documentation are to be licensed as Creative Commons Attribution-ShareAlike 4.0 International License, with exception in regards to the use of copyrighted materials as defined in the following paragraph.

Depictions of software products and other copyrighted materials is used within the United States legal doctrine of fair use. New additions to the documentation are to utilize copyrighted materials in accordance with this legal doctrine.

The build script, make file, and make scripts are licensed under the MIT license, which is included in LICENSE.txt.

The theme that is embedded in this repository is provided under a different license.

## Install and Build

Requires NodeJS@12 and npm@6. 

Install Grunt globally if you have not done so already:

```
 $ npm install -g grunt-cli
```

Then install the remaining dependencies:

```
 $ npm install
```

Finally:

```
 $ grunt
```

The web server should now be connected to `0.0.0.0:8999`. You can connect locally by directing your web browser to `127.0.0.1:8999`. You may edit source files while the web server is running, and the changes will be reflected after refreshing the page.
