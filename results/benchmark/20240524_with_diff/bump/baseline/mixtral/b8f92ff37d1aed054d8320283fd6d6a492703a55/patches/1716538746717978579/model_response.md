Here's the updated method with the necessary changes to fix the error:

```java
private org.apache.maven.plugin.surefire.api.testset.TestListResolver getTestListResolver() {
    return new org.apache.maven.plugin.surefire.provider.TestClassExtensionTestListResolver();
}
```

The original `TestListResolver` has been replaced with `TestClassExtensionTestListResolver` which is available in the updated library version.