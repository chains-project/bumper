It seems that the `Ignore` annotation is not recognized by the compiler. This could be due to a missing dependency or a conflict with another library.

To fix this issue, you can try adding the following dependency to your `pom.xml` file (if you're using Maven) or your build.gradle file (if you're using Gradle):
```xml
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter-engine</artifactId>
    <version>5.7.0</version>
    <scope>test</scope>
</dependency>
```
Alternatively, you can also try using the fully qualified name of the `Ignore` annotation, like this:
```java
@org.junit.jupiter.api.Test
@org.junit.jupiter.api.Ignore
void testRobustnessRandomly() {
    // ...
}
```
This should allow the compiler to recognize the `Ignore` annotation and avoid the error.