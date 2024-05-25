Here's a possible patch for the given failing code:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
In this patch, I created a variable `classInfo` to store the result of `coverage.getClassInfo(Collections.singleton(data.getMutatedClass()))`, and then passed it as an argument to the `MutationTestSummaryData` constructor. This should fix the "cannot find symbol" error, as long as `ClassInfo` is still present in the new version of the external dependency.