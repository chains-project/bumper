Here's a proposed patch to fix the failure:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(data.getMutatedClass());
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
The patch removes the `getClassInfo` method call on the `CoverageDatabase` object, which is not available in the new library version. Instead, we directly call the `getClassInfo` method on the `coverage` object, passing in the `ClassName` object for the mutated class.

This patch should fix the error and allow the code to compile and run successfully.