Here's the proposed patch for the given client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    org.pitest.classinfo.ClassInfoBuilder builder = org.pitest.classinfo.ClassInfoVisitor.getClassInfo(data.getMutatedClass(), new byte[0], 0);
    org.pitest.classinfo.ClassInfo classInfo = builder.build();
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```

This patch replaces the usage of `getClassInfo` method from `CoverageDatabase` with the new `getClassInfo` method from `ClassInfoVisitor`. It first creates a `ClassInfoBuilder` using the new method, then builds a `ClassInfo` instance from it. Finally, it creates the `MutationTestSummaryData` instance using the new `ClassInfo`.