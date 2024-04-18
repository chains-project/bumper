It seems that the error is caused by the missing `isAllBlank` method in the `CreateJFrogPlatformInstanceStep` class. This method is not available in the current version of the P4Java library.

To fix the error, you can try using the `org.jenkinsci.plugins.p4.util.P4Util` class, which provides a similar method called `isAllBlank`. Here's an example of how you can modify the code to use this method:
```java
import org.jenkinsci.plugins.p4.util.P4Util;

...

if (P4Util.isAllBlank(step.url, step.artifactoryUrl, step.distributionUrl)) {
    throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
}
```
Alternatively, you can also use the `String.isEmpty()` method to check if the strings are empty, like this:
```java
if (step.url.isEmpty() && step.artifactoryUrl.isEmpty() && step.distributionUrl.isEmpty()) {
    throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
}
```
I hope this helps! Let me know if you have any further questions.