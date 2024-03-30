Here's a proposed patch to fix the error:
```
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    final ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
The patch removes the `Override` annotation, as it's not necessary, and assigns the result of `coverage.getClassInfo()` to a variable `classInfo` for better readability. The rest of the code remains the same.