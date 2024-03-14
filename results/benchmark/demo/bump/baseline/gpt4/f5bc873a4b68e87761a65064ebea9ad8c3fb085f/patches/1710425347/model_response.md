```java
public MavenProject getProject() {
    if(project == null){
        project = new MavenProject();
    }
    return project;
}
```