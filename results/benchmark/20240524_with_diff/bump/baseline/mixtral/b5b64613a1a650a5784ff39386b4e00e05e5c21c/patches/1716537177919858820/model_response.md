Here's the updated `checkInputs` method with the new `isAllBlank` method implementation using `StringUtils.isAllBlank` from Apache Commons Lang library:

```java
import org.apache.commons.lang3.StringUtils;

private void checkInputs(JFrogPlatformInstance server) throws IOException {
    if (StringUtils.isAllBlank(server.getUrl(), server.getArtifactory().getUrl(), server.getDistribution().getUrl(),
            step.url, step.artifactoryUrl, step.distributionUrl)) {
        throw new IOException("Server URL is missing");
    }
    if (StringUtils.isNotBlank(step.credentialsId)) {
        if (StringUtils.isNotBlank(step.username)) {
            throw new IOException("'rtServer' step can't include both credentialsId and username");
        }
        if (StringUtils.isNotBlank(step.password)) {
            throw new IOException("'rtServer' step can't include both credentialsId and password");
        }
    }
}
```

You need to include the Apache Commons Lang library to use `StringUtils`. You can add it as a dependency in your project. For Maven, add this to your `pom.xml`:

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
    <version>3.12.0</version>
</dependency>
```

For Gradle, add this to your `build.gradle`:

```groovy
implementation 'org.apache.commons:commons-lang3:3.12.0'
```