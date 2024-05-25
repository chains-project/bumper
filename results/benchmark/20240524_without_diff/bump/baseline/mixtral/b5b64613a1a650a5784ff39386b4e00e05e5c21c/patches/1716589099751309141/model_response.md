Here's a possible patch for the given error. I noticed that the `isAllBlank` method is available in `org.apache.commons.lang3.StringUtils` which is part of the Apache Commons Lang library. I'm assuming this library is available in your project's dependencies.

If this library is not available, you can add it to your project by adding the following dependency to your `pom.xml` file (for Maven) or `build.gradle` file (for Gradle):

For Maven:
```xml
<dependency>
  <groupId>org.apache.commons</groupId>
  <artifactId>commons-lang3</artifactId>
  <version>3.12.0</version>
</dependency>
```

For Gradle:
```groovy
implementation 'org.apache.commons:commons-lang3:3.12.0'
```

Here's the patch for the `CreateJFrogInstanceStep` class:
```java
import static org.apache.commons.lang3.StringUtils.isAllBlank;

// ...

@Override
public void execute(StepContext context) throws IOException, InterruptedException {
    // ...
    if (isAllBlank(url, apiKey, url, routerUrl)) {
        // ...
    }
    // ...
}
```
Make sure to replace the import statement at the top of the file to import `org.apache.commons.lang3.StringUtils` instead of `org.apache.commons.text.StringUtils`. The `isAllBlank` method should be available now.