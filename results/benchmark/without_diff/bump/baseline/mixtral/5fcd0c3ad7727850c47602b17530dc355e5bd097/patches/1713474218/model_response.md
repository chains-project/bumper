Here's a patch for the given client code:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    if (classInfo == null) {
        return new MutationTestSummaryData(data.getFileName(), data.getMutations(), new ArrayList<>());
    }
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```

This patch checks if `classInfo` is `null` and returns a new `MutationTestSummaryData` instance with an empty list instead of throwing an error. This change should resolve the error caused by the missing external dependency.