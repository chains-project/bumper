Here's the proposed patch for the failing client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(org.pitest.coverage.CoverageDatabase coverage, org.pitest.classinfo.ClassName className) {
    byte[] classfileBytes = coverage.getClassFile(className);
    long timestamp = coverage.getClassFileTimestamp(className);
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, classfileBytes, timestamp);
}
```

The patch introduces a new helper method `getClassInfoFromCoverage` that replaces the removed `getClassInfo` method from `CoverageDatabase`. The helper method constructs the `ClassInfo` using the new `getClassInfo` static method from `ClassInfoVisitor`.