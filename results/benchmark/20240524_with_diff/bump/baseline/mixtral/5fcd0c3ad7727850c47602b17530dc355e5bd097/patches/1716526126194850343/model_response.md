Here's the proposed patch:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(),
        getClassInfoFromCoverageDatabase(coverage, data.getMutatedClass()));
}

private Collection<ClassInfo> getClassInfoFromCoverageDatabase(CoverageDatabase coverage, ClassName className) {
    return coverage.getClassInfo(className).getUniqueClassInfo();
}
```

The patch includes a new helper method `getClassInfoFromCoverageDatabase` that retrieves the `ClassInfo` using the new method `getClassInfo` added to `CoverageDatabase`. Additionally, the `getClassInfo` method from `CoverageDatabase` is called with a single `ClassName` instead of a `Set` of `ClassName`s.