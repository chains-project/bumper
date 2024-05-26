Here's a possible patch for the given client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    org.pitest.classinfo.ClassInfoBuilder builder = org.pitest.classinfo.ClassInfoVisitor.getClassInfo(data.getMutatedClass(), new byte[0], 0);
    org.pitest.classinfo.ClassInfo classInfo = builder.build();
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassCoverage(classInfo).getClassInfo());
}
```

In this patch, I have used the new `getClassInfo` method from `ClassInfoVisitor` to create a `ClassInfoBuilder` for the `MutatedClass`. I then build the `ClassInfo` from the builder and use it to get the `ClassCoverage` from the `CoverageDatabase`. Finally, I get the `ClassInfo` from the `ClassCoverage`. This way, I avoid using the deprecated `getClassInfo` method from `CoverageDatabase` and use the new method from `ClassInfoVisitor` instead.