Here's a possible patch for the code you provided. I added a new helper method `isAllBlank` that checks if all the given strings are blank or not.

This method uses the `org.apache.commons.lang3.StringUtils.isBlank` method to check if a single string is blank or not.

I also imported the `org.apache.commons.lang3.StringUtils` class at the beginning of the file to use its methods.

Here's the patched code:
```java
import org.apache.commons.lang3.StringUtils;

// ...

private void checkInputs(org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance server) throws java.io.IOException {
    if (isAllBlank(server.getUrl(), server.getArtifactory().getUrl(), server.getDistribution().getUrl(), step.url, step.artifactoryUrl, step.distributionUrl)) {
        throw new java.io.IOException("Server URL is missing");
    }
    if (StringUtils.isNotBlank(step.credentialsId)) {
        if (StringUtils.isNotBlank(step.username)) {
            throw new java.io.IOException("'rtServer' step can't include both credentialsId and username");
        }
        if (StringUtils.isNotBlank(step.password)) {
            throw new java.io.IOException("'rtServer' step can't include both credentialsId and password");
        }
    }
}

private boolean isAllBlank(String... strings) {
    for (String string : strings) {
        if (!StringUtils.isBlank(string)) {
            return false;
        }
    }
    return true;
}
```
This code should fix the compilation error you were facing.

Note that I didn't use any of the added or removed library methods you provided, as they didn't seem relevant to the failing code.