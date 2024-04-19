It seems that the error is caused by the fact that the `Ignore` annotation is not recognized by the compiler. This is likely because the `Ignore` annotation is not a standard Java annotation, but rather a custom annotation defined by the `micycle.pgs` package.

To fix this issue, you can try adding the following line to the `pom.xml` file of your project:
```
<dependency>
    <groupId>micycle.pgs</groupId>
    <artifactId>micycle-pgs</artifactId>
    <version>1.0.0</version>
</dependency:
```
This will add the `micycle-pgs` dependency to your project, which should make the `Ignore` annotation available to the compiler.

Alternatively, you can also try using a different annotation, such as `@org.junit.jupiter.api.Test` instead of `@micycle.pgs.Ignore`. This should also fix the compilation error.