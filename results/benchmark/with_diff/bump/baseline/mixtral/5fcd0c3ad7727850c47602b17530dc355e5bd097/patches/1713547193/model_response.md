Here's the fixed `createSummaryData` method:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(),
        coverage.getClassInfo(data.getMutatedClass()).buildClassInfo());
}
```

The change is using the new `getClassInfo` method on `CoverageDatabase` and calling `buildClassInfo` on the returned `ClassInfoBuilder`.