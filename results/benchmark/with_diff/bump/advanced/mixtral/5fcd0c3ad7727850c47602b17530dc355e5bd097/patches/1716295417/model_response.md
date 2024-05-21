Here's the proposed patch to fix the error:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    org.pitest.classinfo.ClassInfoBuilder builder = org.pitest.classinfo.ClassInfoVisitor.getClassInfo(data.getMutatedClass(), new byte[0], 0);
    coverage.accept(builder);
    org.pitest.classinfo.ClassInfo classInfo = builder.build();
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```

This patch modifies the `createSummaryData` method to use the `ClassInfoBuilder` instead of the removed `getClassInfo` method. It first creates a `ClassInfoBuilder` using the `ClassName` of the mutated class and then uses the `CoverageDatabase` object to populate it with coverage information. Finally, it builds a `ClassInfo` object from the `ClassInfoBuilder` and returns a new `MutationTestSummaryData` object using this `ClassInfo`.