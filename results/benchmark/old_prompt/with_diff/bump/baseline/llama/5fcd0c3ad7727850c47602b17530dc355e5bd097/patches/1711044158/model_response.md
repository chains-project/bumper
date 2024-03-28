Here's a proposed patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    var classInfo = coverage.getClassInfo(data.getMutatedClass());
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
The patch removes the `getClassInfo` method call on the `coverage` object, which is no longer available in the updated library version. Instead, we use the `getClassInfo` method provided by the `CoverageDatabase` class, which takes a `ClassName` parameter. We pass `data.getMutatedClass()` as the parameter to get the `ClassInfo` object for the mutated class.

The rest of the code remains the same.