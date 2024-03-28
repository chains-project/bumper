-- org.apache.myfaces.tobago.maven.plugin.MavenProject
++ org.apache.maven.project.MavenProject

You should change the code to use the new class as follows:
```java
public org.apache.maven.project.MavenProject getProject() {
    return project;
}
```