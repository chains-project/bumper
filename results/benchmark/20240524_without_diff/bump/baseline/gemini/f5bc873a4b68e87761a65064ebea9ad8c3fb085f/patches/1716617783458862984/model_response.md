```java
import org.apache.maven.artifact.DependencyResolutionRequiredException;

  public void execute() throws MojoExecutionException, DependencyResolutionRequiredException {
    File themeDir = new File(getProject().getBasedir(), "src/main/webapp/theme/" + themeName);
    if (!themeDir.exists()) {
      throw new MojoExecutionException("Theme directory " + themeDir + " does not exist.");
    }
    File themeFile = new File(themeDir, themeName + ".zip");
    if (!themeFile.exists()) {
      throw new MojoExecutionException("Theme file " + themeFile + " does not exist.");
    }
    File targetThemeDir = new File(getProject().getBuild().getDirectory(), "theme/" + themeName);
    if (!targetThemeDir.mkdirs()) {
      throw new MojoExecutionException("Failed to create target theme directory " + targetThemeDir);
    }
    try (ZipFile zipFile = new ZipFile(themeFile)) {
      Enumeration<? extends ZipEntry> entries = zipFile.entries();
      while (entries.hasMoreElements()) {
        ZipEntry entry = entries.nextElement();
        File targetFile = new File(targetThemeDir, entry.getName());
        if (entry.isDirectory()) {
          if (!targetFile.mkdirs()) {
            throw new MojoExecutionException("Failed to create target directory " + targetFile);
          }
        } else {
          try (InputStream in = zipFile.getInputStream(entry);
               FileOutputStream out = new FileOutputStream(targetFile)) {
            IOUtils.copy(in, out);
          }
        }
      }
    } catch (IOException e) {
      throw new MojoExecutionException("Failed to unpack theme " + themeName, e);
    }
  }
```