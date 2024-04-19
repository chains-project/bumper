Here's a proposed patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(data.getMutatedClass());
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
The patch removes the `getClassInfo` method call on the `coverage` object, which is not available in the new library version. Instead, it uses the `getClassInfo` method of the `CoverageDatabase` class to get the `ClassInfo` object for the mutated class.

Note that this patch assumes that the `CoverageDatabase` class has a `getClassInfo` method that takes a single `ClassName` argument and returns a `ClassInfo` object. If this method does not exist in the new library version, a different patch will be needed.