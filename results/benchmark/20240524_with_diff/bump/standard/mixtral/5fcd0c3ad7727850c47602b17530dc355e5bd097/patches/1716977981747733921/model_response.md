Here's the proposed patch for the given client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverageDatabase(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverageDatabase(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.classinfo.ClassName className) {
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, coverage.getRawCoverageForClass(className), coverage.getTimestamp());
}
```

This patch introduces a new helper method `getClassInfoFromCoverageDatabase` which utilizes the new `getClassInfo` method from `ClassInfoVisitor`. The helper method takes the `CoverageDatabase` and the `ClassName` to get the corresponding `ClassInfo`. The original `createSummaryData` method has been modified to use the new helper method.