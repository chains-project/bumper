```java
  import org.apache.maven.artifact.DependencyResolutionRequiredException;
  import org.apache.maven.plugin.MojoExecutionException;
  import org.apache.maven.plugins.annotations.Mojo;
  import org.apache.maven.plugins.annotations.Parameter;
  import org.apache.maven.project.MavenProject;
  import org.apache.myfaces.tobago.maven.plugin.AbstractTobagoMojo;
  import org.apache.myfaces.tobago.maven.plugin.TobagoTheme;
  import org.apache.myfaces.tobago.maven.plugin.TobagoTheme.Theme;
  import org.apache.myfaces.tobago.maven.plugin.utils.Utils;

  import java.io.File;
  import java.io.IOException;
  import java.nio.file.Files;
  import java.nio.file.Path;
  import java.nio.file.Paths;
  import java.util.List;
  import java.util.stream.Collectors;

  /**
   * Unpack the theme to the project.
   *
   * @since 1.0.0
   */
  @Mojo(name = "unpack-theme", threadSafe = true)
  public class UnPackThemeMojo extends AbstractTobagoMojo {

    @Parameter(property = "theme", required = true)
    private TobagoTheme theme;

    @Parameter(property = "project", readonly = true)
    private MavenProject project;

    @Override
    public void execute() throws MojoExecutionException {
      final Theme theme = this.theme.getTheme();
      final File themeSource = new File(theme.getThemePath());
      final File themeTarget = new File(project.getBasedir(), "src/main/webapp/resources/" + theme.getThemeDirectory());
      final File themeTargetCss = new File(themeTarget, "css");
      final File themeTargetJs = new File(themeTarget, "js");
      final File themeTargetImg = new File(themeTarget, "img");
      final File themeTargetFonts = new File(themeTarget, "fonts");

      if (themeSource.exists()) {
        try {
          final List<Path> collect = Files.walk(Paths.get(themeSource.getAbsolutePath())).filter(Files::isRegularFile).collect(Collectors.toList());
          for (final Path path : collect) {
            final String relativePath = path.toFile().getAbsolutePath().substring(themeSource.getAbsolutePath().length() + 1);
            final File targetFile = new File(themeTarget, relativePath);
            final File parentFile = targetFile.getParentFile();
            if (!parentFile.exists()) {
              parentFile.mkdirs();
            }
            Files.copy(path, targetFile.toPath());
          }
          final File themeTargetCssSource = new File(themeSource, "css");
          if (themeTargetCssSource.exists()) {
            final List<Path> collectCss = Files.walk(Paths.get(themeTargetCssSource.getAbsolutePath())).filter(Files::isRegularFile).collect(Collectors.toList());
            for (final Path path : collectCss) {
              final String relativePath = path.toFile().getAbsolutePath().substring(themeTargetCssSource.getAbsolutePath().length() + 1);
              final File targetFile = new File(themeTargetCss, relativePath);
              final File parentFile = targetFile.getParentFile();
              if (!parentFile.exists()) {
                parentFile.mkdirs();
              }
              Files.copy(path, targetFile.toPath());
            }
          }
          final File themeTargetJsSource = new File(themeSource, "js");
          if (themeTargetJsSource.exists()) {
            final List<Path> collectJs = Files.walk(Paths.get(themeTargetJsSource.getAbsolutePath())).filter(Files::isRegularFile).collect(Collectors.toList());
            for (final Path path : collectJs) {
              final String relativePath = path.toFile().getAbsolutePath().substring(themeTargetJsSource.getAbsolutePath().length() + 1);
              final File targetFile = new File(themeTargetJs, relativePath);
              final File parentFile = targetFile.getParentFile();
              if (!parentFile.exists()) {
                parentFile.mkdirs();
              }
              Files.copy(path, targetFile.toPath());
            }
          }
          final File themeTargetImgSource = new File(themeSource, "img");
          if (themeTargetImgSource.exists()) {
            final List<Path> collectImg = Files.walk(Paths.get(themeTargetImgSource.getAbsolutePath())).filter(Files::isRegularFile).collect(Collectors.toList());
            for (final Path path : collectImg) {
              final String relativePath = path.toFile().getAbsolutePath().substring(themeTargetImgSource.getAbsolutePath().length() + 1);
              final File targetFile = new File(themeTargetImg, relativePath);
              final File parentFile = targetFile.getParentFile();
              if (!parentFile.exists()) {
                parentFile.mkdirs();
              }
              Files.copy(path, targetFile.toPath());
            }
          }
          final File themeTargetFontsSource = new File(themeSource, "fonts");
          if (themeTargetFontsSource.exists()) {
            final List<Path> collectFonts = Files.walk(Paths.get(themeTargetFontsSource.getAbsolutePath())).filter(Files::isRegularFile).collect(Collectors.toList());
            for (final Path path : collectFonts) {
              final String relativePath = path.toFile().getAbsolutePath().substring(themeTargetFontsSource.getAbsolutePath().length() + 1);
              final File targetFile = new File(themeTargetFonts, relativePath);
              final File parentFile = targetFile.getParentFile();
              if (!parentFile.exists()) {
                parentFile.mkdirs();
              }
              Files.copy(path, targetFile.toPath());
            }
          }
        } catch (final IOException e) {
          throw new MojoExecutionException("Can't unpack theme.", e);
        }
      } else {
        throw new MojoExecutionException("Theme source '" + themeSource + "' doesn't exist.");
      }
    }
  }
```