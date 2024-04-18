Sure, here's a possible patch for the failing client code:
```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    List<MutationInfo> mutations = data.getMutations();
    String fileName = data.getFileName();
    return new MutationTestSummaryData(fileName, mutations, classInfo);
}
```
The patch creates local variables for each argument of the `MutationTestSummaryData` constructor, so that the constructor can be called with separate arguments instead of passing in collections directly. This should avoid any issues with external dependencies that might have been causing the original error.

Note that this patch assumes that the `MutationTestSummaryData` constructor still has the same signature as before, and that the `ClassMutationResults` and `CoverageDatabase` classes have not been modified in a way that would break this code. If those assumptions are incorrect, then a different patch may be necessary.