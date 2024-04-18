Here's the proposed patch for the failing client code:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    if (classInfo == null) {
        // Handle the case when classInfo is null
        return null;
    }
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```

In this patch, we first get the `ClassInfo` object and check if it's `null`. If it is, we handle the case appropriately (you can replace the `return null;` statement with your own error handling logic). If it's not `null`, we proceed with creating the `MutationTestSummaryData` object as before.

This patch assumes that the `ClassInfo` object returned by `coverage.getClassInfo()` can be `null` in the new version of the external dependency. This could be the cause of the "cannot find symbol" error message. By checking for `null` and handling it appropriately, we can avoid the error and ensure that the code is compatible with the new version of the dependency.