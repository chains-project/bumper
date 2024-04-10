Here's a possible patch to fix the error:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final org.pitest.classinfo.ClassInfo classInfo = coverage.getClassInfo(data.getMutatedClass());
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
The patch uses the `getClassInfo` method from the `org.pitest.classinfo` package, which is available in the updated library version. The method takes a `ClassName` parameter and returns a `ClassInfo` object, which can be used to get the class information.

The rest of the code remains the same, as the issue was only with the `getClassInfo` method call.