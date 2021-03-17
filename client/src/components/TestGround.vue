<template>

<v-card
  class="mx-4"
  tile
>
  <v-subheader>
    <v-row 
      align="baseline"
      justify="space-between"
    >
      <v-col cols="12" md="6">
        WINNER
      </v-col>
      <v-col cols="12" md="6">
        <v-row class="ml-3">
          <template v-for="g in this.best_crossbreeds.genes">
            <v-chip
              class="mr-1"
              :color="colors[g]"
              text-color="white"
              :key="JSON.stringify(g)"
            >
              {{g}}
            </v-chip>
          </template>
        </v-row>
      </v-col>
    </v-row>
  </v-subheader>

  <v-list two-line>
    <v-list-item-group
      v-model="selected"
      multiple
    >
      <template v-for="(item, index) in winner_combination">
        <v-list-item :key="item.title">
          <template v-slot:default="{ }">
            <v-list-item-content>
              <v-row class="ml-3">
                <template v-for="gene in item.genes">
                  <v-chip
                    class="mr-1"
                    :color="colors[gene]"
                    text-color="white"
                    :key="JSON.stringify(gene)"
                  >
                    {{ gene }}
                  </v-chip>
                </template>
              </v-row>
            </v-list-item-content>
          </template>
        </v-list-item>

        <v-divider
          v-if="index + 1 < items.length"
          :key="index"
        ></v-divider>
      </template>
    </v-list-item-group>
  </v-list>
</v-card>



















<template>
  <v-card
    class="mx-auto"
    outlined
  >
    <v-list-item three-line>
      <v-list-item-content>
        <div class="overline mb-4">RESULTS</div>
        <v-list-item-title class="headline mb-1">Best Gene</v-list-item-title>
        <v-list-item-subtitle>
          <v-row class="ml-3">
            <template v-for="g in this.best_crossbreeds.genes">
              <v-chip
                class="mr-1"
                :color="colors[g]"
                text-color="white"
                :key="JSON.stringify(g)"
              >
                {{g}}
              </v-chip>
            </template>
          </v-row>
        </v-list-item-subtitle>
      </v-list-item-content>

      <v-list-item-avatar
        tile
        size="80"
        color="green"
      ></v-list-item-avatar>
    </v-list-item>

    <v-card-actions>
      <v-btn text>Button</v-btn>
      <v-btn text>Button</v-btn>
    </v-card-actions>
  </v-card>
</template>

</template>