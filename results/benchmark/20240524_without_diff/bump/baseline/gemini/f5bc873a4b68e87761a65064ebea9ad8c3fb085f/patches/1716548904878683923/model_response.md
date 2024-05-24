```java
import org.apache.maven.artifact.Artifact;

  public void execute() throws MojoExecutionException {
    try {
      File source = new File(project.getBuild().getOutputDirectory(), "META-INF/resources/tobago/theme/" + themeName);
      if (themeName.equals(DEFAULT_THEME_NAME)) {
        source = new File(project.getBuild().getOutputDirectory(), "META-INF/resources/tobago/" + themeName);
      }

      File destination = new File(themeDirectory, themeName);
      if (themeName.equals(DEFAULT_THEME_NAME)) {
        destination = new File(themeDirectory, "");
      }

      if (destination.exists()) {
        FileUtils.deleteDirectory(destination);
      }
      FileUtils.copyDirectoryToDirectory(source, destination);

      if (themeName.equals(DEFAULT_THEME_NAME)) {
        File source2 = new File(project.getBuild().getOutputDirectory(), "META-INF/resources/tobago/" + themeName + "/tobago.css");

        File destination2 = new File(themeDirectory, "tobago.css");

        if (source2.exists() && destination2.exists()) {
          String content1 = FileUtils.readFileToString(source2, "UTF-8");
          String content2 = FileUtils.readFileToString(destination2, "UTF-8");

          if (!content1.equals(content2)) {
            throw new MojoExecutionException("tobago.css is different in META-INF/resources/tobago and META-INF/resources/tobago/theme/default");
          }
        }
      }

      for (Artifact artifact : project.getArtifacts()) {
        if (artifact.getArtifactId().startsWith("tobago-theme")) {
          String theme = artifact.getArtifactId().substring("tobago-theme-".length());
          File themeDir = new File(themeDirectory, theme);
          if (!themeDir.exists()) {
            themeDir.mkdir();
          }
          File source3 = new File(artifact.getFile(), "META-INF/resources/tobago/theme/" + theme);
          if (theme.equals(DEFAULT_THEME_NAME)) {
            source3 = new File(artifact.getFile(), "META-INF/resources/tobago/" + theme);
          }
          FileUtils.copyDirectoryToDirectory(source3, destination);
        }
      }

      if (project.getActiveProfiles().contains(PROFILE_ID_LEGACY_CSS)) {
        File source4 = new File(themeDirectory, themeName + "/tobago.css");
        File source5 = new File(themeDirectory, themeName + "/tobago-legacy.css");
        File destination3 = new File(themeDirectory, themeName + "/tobago-legacy.css");
        if (!source4.exists() || !destination3.exists() || !source4.equals(destination3)) {
          FileUtils.copyFile(source5, destination3);
        }

        String content3 = FileUtils.readFileToString(source4, "UTF-8");
        String content4 = FileUtils.readFileToString(destination3, "UTF-8");

        if (!content3.equals(content4)) {
          throw new MojoExecutionException("tobago-legacy.css is different in " + source4.getAbsolutePath() + " and " + destination3.getAbsolutePath());
        }
      }
    } catch (IOException e) {
      throw new MojoExecutionException("Could not unpack theme " + themeName, e);
    }
  }
```