<template>
  <v-app id="inspire">
    <v-main>
      <v-container
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >
          <v-col
            cols="12"
            sm="8"
            md="9"
          >
            <v-card class="elevation-12">
              <v-toolbar
                color="primary"
                dark
                flat
              >
                <v-toolbar-title>RUST Genetics Assistant 1.0</v-toolbar-title>
                <v-spacer></v-spacer>
                <v-tooltip bottom>
                  <template v-slot:activator="{ on }">
                    <v-btn
                      :href="source"
                      icon
                      large
                      target="_blank"
                      v-on="on"
                    >
                      <v-icon>mdi-code-tags</v-icon>
                    </v-btn>
                  </template>
                  <span>Source</span>
                </v-tooltip>
              </v-toolbar>
              <v-card-text>
                <v-row
                  class="px-10"
                  align="baseline"
                  justify="space-between"
                >
                  <v-col
                    cols="12"
                    sm="3"
                    md="6"
                  >
                    <v-container class="pa-5">
                      <v-chip
                        class="ma-1 pa-5"
                        color="green"
                        text-color="white"
                        @click="add_g"
                        large
                      >
                        G
                      </v-chip>
                      <v-chip
                        class="ma-1 pa-5"
                        color="green"
                        text-color="white"
                        @click="add_y"
                        large
                      >
                        Y
                      </v-chip>
                      <v-chip
                        class="ma-1 pa-5"
                        color="green"
                        text-color="white"
                        @click="add_h"
                        large
                      >
                        H   
                      </v-chip>
                      <v-chip
                        class="ma-1 ml-6 pa-5"
                        color="red"
                        text-color="white"
                        @click="add_x"
                        large
                      >
                        X
                      </v-chip>
                      <v-chip
                        class="ma-1 pa-5"
                        color="red"
                        text-color="white"
                        @click="add_w"
                        large
                      >
                        W
                      </v-chip>
                    </v-container>
                    <v-form 
                      class=" pa-5 pl-8"
                      v-model="valid"
                    >
                      <v-row>
                        <v-combobox
                          v-model="select"
                          :items="items"
                          :rules="geneRules"
                          label="Click on the genes above to add them here"
                          multiple
                          outlined
                          chips
                          clearable
                          hide-no-data
                        >
                          <template v-slot:selection="data">
                            <v-chip
                              :color="data.item.color"
                              text-color="white"
                              :key="JSON.stringify(data.item)"
                              v-bind="data.attrs"
                              :input-value="data.selected"
                              :disabled="data.disabled"
                              @click="remove_gene(data.item)"
                            >
                              {{ data.item.text }}
                            </v-chip>
                          </template>
                        </v-combobox>
                        <v-btn
                          class="ml-5"
                          :disabled="!valid"
                          color="success"
                          fab
                          @click="validate"
                        >
                          <v-icon dark>mdi-plus</v-icon>
                        </v-btn>
                      </v-row>
                    </v-form>
                  </v-col>
                </v-row>
                <v-row
                  class="px-10"
                >
                  <v-col
                    cols="12"
                    sm="4"
                    md="4"
                  >
                    <v-card
                      min-height="500"
                      class="mx-auto"
                      outlined
                    >
                      <v-list-item three-line>
                        <v-list-item-content>
                          <div class="overline mb-4">GENE POOL</div>
                          <v-list-item-title class="headline mb-1">Available clones</v-list-item-title>
                          <v-list-item-subtitle>Add clones (preferably with at least 5 greens) to crossbreed.</v-list-item-subtitle>
                          <v-list-item-subtitle class="mt-2">The more you add, the more options you have to find the perfect gene.</v-list-item-subtitle>
                          <v-divider class="mt-3"></v-divider>
                          <v-row class="ml-0 mt-2 ">
                            <template v-for="(item, index) in genes">
                              <v-list-item :key="item.title" class="pl-0">
                                <template v-slot:default="{ }">
                                  <v-list-item-content>
                                    <v-row class="ml-0">
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
                                      <v-btn 
                                        class="ml-3" 
                                        icon color="gray"
                                        @click="remove_clone(item)">
                                        <v-icon>mdi-delete</v-icon>
                                      </v-btn>
                                    </v-row>
                                  </v-list-item-content>
                                </template>
                              </v-list-item>

                              <v-divider
                                v-if="index + 1 < items.length"
                                :key="index"
                              ></v-divider>
                            </template>

                          </v-row>

                        </v-list-item-content>

                        <v-list-item-avatar
                          tile
                          size="80"
                          color="white"
                        >
                          <v-img src="https://www.shareicon.net/data/512x512/2015/12/27/693929_plant_512x512.png"></v-img>
                        </v-list-item-avatar>
                      </v-list-item>

                      <v-card-actions>
                      </v-card-actions>
                    </v-card>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="4"
                    md="4"
                  >
                    <v-card
                      class="mx-auto"
                      outlined
                      min-height="500"
                    >
                      <v-list-item three-line>
                        <v-list-item-content>
                          <div class="overline mb-4">FIRST STEP</div>
                          <v-list-item-title class="headline mb-1">Best Gene</v-list-item-title>
                          <v-list-item-subtitle>Crossbreed to obtain a gene with 6 greens</v-list-item-subtitle>
                          <v-list-item-subtitle>
                            <v-row class="ml-0 mt-2">
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
                          <v-divider class="mt-3"></v-divider>
                          <v-subheader 
                            class="ml-0 pl-0"
                            v-if="winner_combination.length != 0"
                          >
                            Crossbreed the following clones to get the best clone
                          </v-subheader>
                          <v-subheader 
                            class="ml-0 pl-0"
                            v-else-if="genes.length == 0"
                          >
                            Add clones to compute best crossbreeding options
                          </v-subheader>
                          <v-subheader 
                            class="ml-0 pl-0"
                            v-else
                          >
                            No need to crossbreed. You already have the best gene.
                          </v-subheader>
                          <v-row class="ml-0 mt-2 ">
                            <template v-for="(item, index) in winner_combination">
                              <v-list-item :key="item.title" class="pl-0">
                                <template v-slot:default="{ }">
                                  <v-list-item-content>
                                    <v-row class="ml-0">
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

                          </v-row>

                        </v-list-item-content>

                        <v-list-item-avatar
                          tile
                          size="80"
                          color="white"
                        >
                          <v-img src="https://www.freepnglogos.com/uploads/dna-png/biology-dna-genetic-genome-studing-icon-32.png"></v-img>
                        </v-list-item-avatar>
                      </v-list-item>

                      <v-card-actions>
                      </v-card-actions>
                    </v-card>

                  </v-col>
                  <v-col
                    cols="12"
                    sm="4"
                    md="4"
                  >
                    <v-card
                      class="mx-auto"
                      outlined
                      min-height="500"
                    >
                      <v-list-item three-line>
                        <v-list-item-content>
                          <div class="overline mb-4">50/50 TECHNIQUE</div>
                          <v-list-item-title class="headline mb-1">Result</v-list-item-title>
                          <v-list-item-subtitle>Crossbreed using the 50/50 techenique to obtain improve your 6-green gene</v-list-item-subtitle>
                          <v-list-item-subtitle>
                            <v-row class="ml-0 mt-2">
                              <template v-for="gg in best_5050.genes">
                                <v-chip
                                  class="mr-1"
                                  :color="colors[gg]"
                                  text-color="white"
                                  :key="JSON.stringify(gg)"
                                >
                                  {{gg}}
                                </v-chip>
                              </template>
                            </v-row>
                          </v-list-item-subtitle>
                          <v-divider class="mt-3"></v-divider>
                          <v-subheader 
                            class="ml-0 pl-0"
                            v-if="winner_5050_combination.length != 0"
                          >
                            Crossbreed the following clones to have a 50% change of thetting a better clone
                          </v-subheader>
                          <v-subheader 
                            class="ml-0 pl-0"
                            v-else
                          >
                            You don't have enough clones to perform the 50/50 technique.
                          </v-subheader>
                          <v-row class="ml-0 mt-2 ">
                            <template v-for="(itm, idx) in winner_5050_combination">
                              <v-list-item :key="itm.title" class="pl-0">
                                <template v-slot:default="{ }">
                                  <v-list-item-content>
                                    <v-row class="ml-0">
                                      <template v-for="gene5050 in itm.genes">
                                        <v-chip
                                          class="mr-1"
                                          :color="colors[gene5050]"
                                          text-color="white"
                                          :key="JSON.stringify(gene5050)"
                                        >
                                          {{ gene5050 }}
                                        </v-chip>
                                      </template>
                                    </v-row>
                                  </v-list-item-content>
                                </template>
                              </v-list-item>
                              <v-divider
                                v-if="idx + 1 < itm.length"
                                :key="idx"
                              ></v-divider>
                            </template>

                          </v-row>

                        </v-list-item-content>

                        <v-list-item-avatar
                          tile
                          size="80"
                          color="white"
                        >
                          <v-img src="https://familyresourcectr.org/wp-content/uploads/2016/05/homepage-icons-50-percent.png"></v-img>
                        </v-list-item-avatar>
                      </v-list-item>

                      <v-card-actions>
                      </v-card-actions>
                    </v-card>

                  </v-col>
                </v-row>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
  import axios from 'axios'
  // import CardList from '@/components/CardList'
export default {
    name: 'HelloWorld',
    components: {
      // CardList
    },
    data: () => ({
      colors: {"G": "green", "Y": "green", "H": "green", "X": "red", "W": "red"},
      best_crossbreeds: {},
      winner_combination: [],
      best_5050: {},
      winner_5050_combination: [],
      genes: [],
      select: [],
      items: [],
      _chip_color: "",
      valid: true,
      geneRules: [
        v => (v || '').length == 6 ||
            `You must select 6 genes`,
      ],
    }),

    methods: {
      populate_cb() {
        if (this.best_crossbreeds.combination == null) {return;}
        for (var i = 0; i < this.best_crossbreeds.combination.length; i++) {
          this.winner_combination.push({
            'genes': this.best_crossbreeds.combination[i]
          });
        }
        return;
      },
      populate_5050() {
        if (this.best_5050.combination == null) {return;}
        for (var j = 0; j < this.best_5050.combination.length; j++) {
          this.winner_5050_combination.push({
            'genes': this.best_5050.combination[j]
          });
        }
        return;
      },
      calculate () {
        this.winner_combination = []
        this.best_crossbreeds = {}
        this.winner_5050_combination = []
        this.best_5050 = {}
        
        var genes_list = []
        for (var i = 0; i < this.genes.length; i++) {
            genes_list.push(this.genes[i].genes)
        }

        axios.post('http://127.0.0.1:5000/ping', {
          genes: genes_list
        })
        .then((response) => {
          this.best_crossbreeds = response.data.best_crossbreeds;
          this.best_5050        = response.data.best_5050;
          console.info(JSON.stringify(this.best_5050));
          this.populate_cb();
          this.populate_5050();
          console.info(JSON.stringify(this.winner_5050_combination))
        });
        
      },
      validate () {
        var clone = ""
        var i;
        for (i = 0; i < this.select.length; i++) {
          clone += this.select[i].text
        }
        // alert(clone)
        this.genes.push({
          'genes': clone
        })
        this.calculate()
        this.select = []
        this.$refs.form.validate();
      },
      remove_gene (item) {
        this.select.splice(this.select.indexOf(item), 1)
        this.select = [...this.select]
      },
      remove_clone (item) {
        this.genes.splice(this.genes.indexOf(item), 1)
        this.genes = [...this.genes]
        this.calculate()
      },
      clear () {
        this.genes = []
      },
      add_g() {
        this.select.push({
            text: 'G',
            color: 'green',
          })
      },
      add_y() {
        this.select.push({
            text: 'Y',
            color: 'green',
          })
      },
      add_h() {
        this.select.push({
            text: 'H',
            color: 'green',
          })
      },
      add_x() {
        this.select.push({
            text: 'X',
            color: 'red',
          })
      },
      add_w() {
        this.select.push({
            text: 'W',
            color: 'red',
          })
      }
    }
}
</script>