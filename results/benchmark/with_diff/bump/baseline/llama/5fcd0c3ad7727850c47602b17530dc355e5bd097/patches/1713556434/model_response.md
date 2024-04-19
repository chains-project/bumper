Here's a possible patch to fix the error:
```
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(data.getMutatedClass());
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
The patch removes the `getClassInfo(Collections.singleton(data.getMutatedClass()));` call, which is not available in the new library version, and instead uses the `getClassInfo(data.getMutatedClass());` method, which is added in the new version.

It's important to note that this patch assumes that the `CoverageDatabase` object has the `getClassInfo(ClassName)` method, which is added in the new version. If this method is not available, a different patch would be needed.