Here is the proposed patch for the failing client code:
```java
import java.io.File;
import org.codehaus.plexus.util.FileUtils;

// ...

File resourcesDir = new File(basedir, "src/main/resources");
File themeDir = new File(resourcesDir, "META-INF/resources/org/apache/myfaces/tobago/theme");
File targetDir = new File(basedir, "target/theme");

if (!themeDir.exists()) {
    throw new MojoFailureException("Unable to find theme directory: " + themeDir.getAbsolutePath());
}

if (!targetDir.exists()) {
    FileUtils.forceMkdir(targetDir);
}

File[] themeFiles = themeDir.listFiles();
for (File themeFile : themeFiles) {
    File targetFile = new File(targetDir, themeFile.getName());
    FileUtils.copyFile(themeFile, targetFile);
}
```
The changes made to the code include:

* Importing the `FileUtils` class from the `org.codehaus.plexus.util` package.
* Creating a `File` object for the `targetDir` variable.
* Checking if the `targetDir` directory exists before copying files to it.
* Creating a `File` object for each `themeFile` in the `themeFiles` array.
* Using the `FileUtils.copyFile` method to copy each `themeFile` to the corresponding `targetFile`.

These changes should fix the error message by updating the code to use the new library version.