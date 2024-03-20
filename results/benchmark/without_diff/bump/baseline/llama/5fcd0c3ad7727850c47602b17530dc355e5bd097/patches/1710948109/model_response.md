Here's a proposed patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    final ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
The issue with the original code is that the `CoverageDatabase` class has changed, and the method `getClassInfo()` is no longer available. The proposed patch uses the `getClassInfo()` method from the `CoverageDatabase` class to retrieve the `ClassInfo` object, which is then passed to the `MutationTestSummaryData` constructor.

This patch fixes the error by providing a valid `ClassInfo` object to the constructor, which was previously null.