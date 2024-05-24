Here's the proposed patch:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(),
        coverage.getClassInfo(data.getMutatedClass()).buildClassInfo());
}
```

In the new library version, the `getClassInfo` method of `CoverageDatabase` returns a `ClassInfoBuilder` instead of a `Collection` of `ClassInfo`. To fix the issue, we can call the `buildClassInfo` method on the returned `ClassInfoBuilder` to get the `ClassInfo` object.