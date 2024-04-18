Here's a proposed patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(data.getMutatedClass());
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
The patch removes the `getClassInfo` method call on the `coverage` object, which is no longer available in the updated library version. Instead, we directly call the `getClassInfo` method on the `coverage` object, passing in the `ClassName` object for the mutated class. This should fix the error and allow the code to compile successfully.