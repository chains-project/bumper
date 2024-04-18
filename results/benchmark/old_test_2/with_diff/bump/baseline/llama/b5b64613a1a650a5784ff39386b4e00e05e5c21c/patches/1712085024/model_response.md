It seems that the error is caused by the missing `isAllBlank` method in the `CreateJFrogPlatformInstanceStep` class. This method is not available in the latest version of the P4Java library, which is being used in the build.

To fix the error, you can try using the `isEmpty` method instead of `isAllBlank`. Here's an example of how you can modify the code to use `isEmpty`:
```java
if (step.url == null || step.artifactoryUrl == null || step.distributionUrl == null) {
    throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
}

if (isEmpty(step.url) || isEmpty(step.artifactoryUrl) || isEmpty(step.distributionUrl)) {
    throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
}
```
Alternatively, you can also use the `StringUtils.isBlank` method from the Apache Commons Lang library to check if the strings are blank. Here's an example:
```java
import org.apache.commons.lang.StringUtils;

if (step.url == null || step.artifactoryUrl == null || step.distributionUrl == null) {
    throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
}

if (StringUtils.isBlank(step.url) || StringUtils.isBlank(step.artifactoryUrl) || StringUtils.isBlank(step.distributionUrl)) {
    throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
}
```
By using `isEmpty` or `StringUtils.isBlank`, you can check if any of the strings are blank, and throw an exception if any of them are blank. This should fix the error and allow the build to complete successfully.