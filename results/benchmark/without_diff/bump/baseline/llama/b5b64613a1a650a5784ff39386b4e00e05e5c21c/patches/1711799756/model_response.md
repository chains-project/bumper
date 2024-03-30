Here's a proposed patch to fix the error:
```java
private void checkInputs(JFrogPlatformInstance server) throws IOException {
        if (isAllBlank(server.getUrl(), server.getArtifactory().getUrl(), server.getDistribution().getUrl(),
                step.url, step.artifactoryUrl, step.distributionUrl)) {
            throw new IOException("Server URL is missing");
        }
        if (isNotBlank(step.credentialsId)) {
            if (isNotBlank(step.username)) {
                throw new IOException("'rtServer' step can't include both credentialsId and username");
            }
            if (isNotBlank(step.password)) {
                throw new IOException("'rtServer' step can't include both credentialsId and password");
            }
        }
    }

    private boolean isAllBlank(String... strings) {
        for (String str : strings) {
            if (String.valueOf(str).isEmpty()) {
                continue;
            }
            return false;
        }
        return true;
    }

    private boolean isNotBlank(String str) {
        return !String.valueOf(str).isEmpty();
    }
```
The patch creates two new methods, `isAllBlank` and `isNotBlank`, to replace the usage of `isBlank` and `isNotBlank` methods that are not available in the updated library version. The `isAllBlank` method takes an array of strings as input and returns `true` if all the strings are empty, and `false` otherwise. The `isNotBlank` method takes a single string as input and returns `true` if the string is not empty, and `false` otherwise.


The `checkInputs` method is then modified to use these new methods to check if the inputs are valid. The `isAllBlank` method is used to check if all the URLs are empty, and the `isNotBlank` method is used to check if the credentials ID, username, and password are not empty.


This patch should fix the error and allow the code to compile without any issues.