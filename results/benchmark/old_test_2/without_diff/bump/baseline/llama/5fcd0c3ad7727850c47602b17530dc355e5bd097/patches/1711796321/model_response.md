Here's a proposed patch to fix the error:
```
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), coverage.getClassInfo(Collections.singleton(data.getMutatedClass())),
        Collections.emptyList());
}
```
The patch adds an empty list as the fourth parameter to the constructor of `MutationTestSummaryData`. This is because the `getClassInfo` method of `CoverageDatabase` now returns a list of `ClassInfo` objects, whereas before it returned a single `ClassInfo` object. The patch ensures that the method still compiles and runs correctly even if the `getClassInfo` method returns multiple `ClassInfo` objects.