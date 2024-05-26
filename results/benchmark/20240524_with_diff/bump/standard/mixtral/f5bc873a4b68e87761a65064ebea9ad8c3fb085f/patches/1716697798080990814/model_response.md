Here is a patch for the client code:

```java
import org.apache.maven.project.MavenProject;
import org.apache.maven.project.MavenProjectBuilder;
import org.codehaus.plexus.util.FileUtils;

// ...

MavenProject project = null;
try {
    FileUtils fileUtils = new FileUtils();
    File pomFile = fileUtils.getFile(projectDir, "pom.xml");
    MavenProjectBuilder projectBuilder = new MavenProjectBuilder();
    project = projectBuilder.build(pomFile);
} catch (Exception e) {
    // handle exception
}
```

Note: This patch adds the `MavenProjectBuilder` class from the same package as `MavenProject`. The `FileUtils` class is also added to help with file operations. These changes should help fix the error message you provided.

Note2: The `projectDir` variable should be initialized before the `try` block.

Note3: This patch assumes that the `pom.xml` file is located in the same directory as the `projectDir` variable.