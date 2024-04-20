Here's a proposed patch for the given client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    org.pitest.classinfo.ClassInfoBuilder builder = org.pitest.classinfo.ClassInfo.forName(data.getMutatedClass());
    coverage.accept(new org.pitest.coverage.CoverageVisitor() {
        @Override
        public void visit(org.pitest.classinfo.ClassInfo classInfo, org.pitest.coverage.CoverageVisitor.Measurement measurement) {
            if (classInfo.getName().equals(data.getMutatedClass())) {
                builder.withMeasurement(measurement);
            }
        }
    });
    org.pitest.classinfo.ClassInfo classInfo = builder.build();
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```

This patch uses the new `ClassInfoBuilder` to build the `ClassInfo` object for the mutated class, and then uses the `CoverageVisitor` to visit each `ClassInfo` and get the measurement for the mutated class.