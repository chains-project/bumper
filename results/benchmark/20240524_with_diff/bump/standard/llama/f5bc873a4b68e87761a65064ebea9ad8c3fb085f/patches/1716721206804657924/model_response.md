```java
public org.apache.maven.execution.MavenSession getProject() {
    return MavenSessionFactory.getMavenSession().getCurrentProject();
}
```