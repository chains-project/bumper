Here's a possible patch to fix the error:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfo(org.pitest.classinfo.ClassName.fromClassName(data.getMutatedClass())));
}
```
The patch uses the `org.pitest.classinfo.ClassName.fromClassName()` method to convert the `data.getMutatedClass()` to a `org.pitest.classinfo.ClassName` object, which can be passed to the `getClassInfo()` method.

Note that this patch assumes that the `org.pitest.classinfo.ClassName` class is available in the classpath, which might not be the case if the dependency update removed it. In that case, you might need to add an additional dependency to the project to use the `ClassName` class.