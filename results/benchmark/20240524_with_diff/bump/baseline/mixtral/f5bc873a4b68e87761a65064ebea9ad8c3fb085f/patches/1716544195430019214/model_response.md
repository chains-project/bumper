Here's the fixed `unpackTheme` method with the required changes:

```java
@Override
public void unpackTheme(Theme theme, File outputDirectory) throws MojoExecutionException, ArtifactResolverException {
    try (InputStream inputStream = theme.getThemeStream();
         ZipInputStream zipInputStream = new ZipInputStream(inputStream)) {
        ZipEntry zipEntry;
        while ((zipEntry = zipInputStream.getNextEntry()) != null) {
            if (zipEntry.isDirectory()) {
                continue;
            }

            String entryName = zipEntry.getName();
            int lastSlashIndex = entryName.lastIndexOf('/');
            String fileName = entryName.substring(lastSlashIndex + 1);
            File destFile = new File(outputDirectory, fileName);

            try (InputStream entryStream = zipInputStream;
                 OutputStream outputStream = new FileOutputStream(destFile)) {

                IOUtils.copy(entryStream, outputStream);
            }
        }
    } catch (IOException e) {
        throw new MojoExecutionException("Error unpacking theme", e);
    }
}
```

The main changes are:

1. Replace the deprecated `getThemeStream()` method with `theme.getThemeStream()`.
2. Replace the removed `IOUtils.copyLarge(input, output)` method with `IOUtils.copy(entryStream, outputStream)`.
3. Import the necessary classes:

```java
import org.apache.commons.io.IOUtils;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
```