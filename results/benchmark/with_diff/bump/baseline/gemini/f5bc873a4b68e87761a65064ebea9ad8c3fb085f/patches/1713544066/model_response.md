```java
  import org.apache.maven.artifact.DependencyResolutionRequiredException;

  import java.util.List;

public class UnPackThemeMojo extends AbstractThemeMojo {

  @Override
  public void execute() throws Exception {
    super.execute();

    List<Artifact> artifacts = project.getArtifacts();
    for (Artifact artifact : artifacts) {
      if (artifact.getGroupId().equals("org.apache.myfaces.tobago") && artifact.getArtifactId().equals("tobago-core")) {
        projectHelper.attachArtifact(project, artifact, "tobago-core");
      }
    }
  }

}
```