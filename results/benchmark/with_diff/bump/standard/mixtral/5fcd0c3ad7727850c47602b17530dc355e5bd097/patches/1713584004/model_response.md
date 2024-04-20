Here's the proposed patch for the given client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(org.pitest.coverage.CoverageDatabase coverage, org.pitest.classinfo.ClassName className) {
    byte[] classBytes = coverage.getClassBytes(className);
    long classTime = coverage.getTimestamp(className);
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, classBytes, classTime);
}
```

This patch replaces the direct usage of the removed `getClassInfo` method from `CoverageDatabase` with a custom method `getClassInfoFromCoverage`. The new method retrieves the class bytes and timestamp from the coverage database and then uses the new `getClassInfo` static method from `ClassInfoVisitor` to build the `ClassInfo` object.